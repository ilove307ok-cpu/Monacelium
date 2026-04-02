#!/usr/bin/env python3
"""
Monacelium Reticulum 測試節點
最小可行實現 (MVP) - 驗證 LoRa Mesh 通訊可行性

使用方法:
    python3 test_node.py --mode announce
    python3 test_node.py --mode listen

需求:
    pip install rns --break-system-packages
"""

import RNS
import argparse
import time
import sys

# Monacelium 配置
APP_NAME = "monacelium.test"
ANNOUNCE_INTERVAL = 30  # 每 30 秒廣播一次身份


class MonaceliumNode:
    """Monacelium 測試節點"""
    
    def __init__(self, mode="announce"):
        self.mode = mode
        
        # 初始化 Reticulum
        print("[Monacelium] 正在初始化 Reticulum Network Stack...")
        RNS.loglevel = RNS.LOG_INFO
        
        # 啟動 Reticulum (會自動讀取 ~/.reticulum/config)
        self.reticulum = RNS.Reticulum()
        
        # 創建本地身份
        self.identity = RNS.Identity()
        
        print(f"[Monacelium] 節點身份: {RNS.prettyhexrep(self.identity.hash)}")
        print(f"[Monacelium] 公鑰: {RNS.prettyhexrep(self.identity.get_public_key()[:16])}...")
        
        # 創建 Destination (通訊端點)
        self.destination = RNS.Destination(
            self.identity,
            RNS.Destination.IN,
            RNS.Destination.SINGLE,
            APP_NAME,
            "node"
        )
        
        # 註冊訊息接收處理器
        self.destination.set_packet_callback(self.packet_received)
        
        print(f"[Monacelium] Destination 已建立: {RNS.prettyhexrep(self.destination.hash)}")
        print(f"[Monacelium] 模式: {self.mode}")
        print("-" * 60)
    
    def packet_received(self, data, packet):
        """處理接收到的封包"""
        try:
            message = data.decode('utf-8')
            sender_hash = RNS.prettyhexrep(packet.destination_hash)
            
            print(f"\n[收到訊息]")
            print(f"  發送者: {sender_hash}")
            print(f"  內容: {message}")
            print(f"  RSSI: {packet.rssi if hasattr(packet, 'rssi') else 'N/A'} dBm")
            print(f"  SNR: {packet.snr if hasattr(packet, 'snr') else 'N/A'} dB")
            print("-" * 60)
            
        except Exception as e:
            print(f"[錯誤] 解析封包失敗: {e}")
    
    def announce(self):
        """廣播節點身份"""
        print(f"[Monacelium] 廣播節點存在...")
        self.destination.announce()
        print(f"[Monacelium] 已發送 Announce (其他節點可發現此節點)")
    
    def send_ping(self, destination_hash):
        """發送 Ping 訊息到指定節點"""
        try:
            # 將十六進位字串轉為 bytes
            dest_hash_bytes = bytes.fromhex(destination_hash)
            
            # 建立 PacketReceipt 以追蹤傳送狀態
            packet = RNS.Packet(dest_hash_bytes, f"PING from {RNS.prettyhexrep(self.identity.hash)}".encode('utf-8'))
            receipt = packet.send()
            
            print(f"[Monacelium] Ping 已發送到 {destination_hash}")
            return receipt
            
        except Exception as e:
            print(f"[錯誤] 發送失敗: {e}")
            return None
    
    def run_announce_mode(self):
        """運行廣播模式 (持續廣播自己的存在)"""
        print("[模式] 持續廣播 (Announce Mode)")
        print("其他節點可以發現並連接到此節點\n")
        
        try:
            while True:
                self.announce()
                print(f"下次廣播: {ANNOUNCE_INTERVAL} 秒後...\n")
                time.sleep(ANNOUNCE_INTERVAL)
                
        except KeyboardInterrupt:
            print("\n[Monacelium] 節點關閉")
    
    def run_listen_mode(self):
        """運行監聽模式 (等待接收訊息)"""
        print("[模式] 監聽模式 (Listen Mode)")
        print("等待其他節點的訊息...\n")
        
        try:
            while True:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n[Monacelium] 節點關閉")


def main():
    parser = argparse.ArgumentParser(description='Monacelium Reticulum 測試節點')
    parser.add_argument(
        '--mode',
        choices=['announce', 'listen'],
        default='announce',
        help='運行模式: announce (廣播) 或 listen (監聽)'
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Monacelium Reticulum 測試節點 v0.1")
    print("=" * 60)
    print()
    
    try:
        node = MonaceliumNode(mode=args.mode)
        
        if args.mode == 'announce':
            node.run_announce_mode()
        else:
            node.run_listen_mode()
            
    except Exception as e:
        print(f"\n[嚴重錯誤] {e}")
        print("\n請確認:")
        print("1. 已安裝 Reticulum: pip install rns --break-system-packages")
        print("2. LoRa 硬體已正確連接 (或使用 UDP 介面測試)")
        sys.exit(1)


if __name__ == "__main__":
    main()