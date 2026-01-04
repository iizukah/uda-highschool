#!/usr/bin/env python3
import asyncio
import websockets

async def handler(websocket):
    async for message in websocket:
        # ここでラズパイ側のターミナルに表示
        print(f"[受信] {message}")

        # クライアントに返信（リアルタイム性を見せるためそのまま返す）
        reply = f"サーバ受信: {message}"
        await websocket.send(reply)
        print(f"[送信] {reply}")

async def main():
    # 0.0.0.0 で全インターフェースから受け付け
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("WebSocket server running on port 8765...")
        await asyncio.Future()  # 永久に待機

if __name__ == "__main__":
    asyncio.run(main())