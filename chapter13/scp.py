# SCPコマンドを実行するプログラム

# ライブラリのインポート
import pexpect

# ローカルのファイル名
local_filename = './scp2.txt'

# サーバー設定
ID = 'students'
PASSWORD = 'winstudents'
HOST = 'www.wincloud.site'
DIR = 'public_html'

# 受講生ディレクトリ(ご自身の受講番号に変更してください)
students_dir = 'IoTiizuka'

# ファイル名
server_filename = 'scp2.txt'

print("SCPコマンドを実行します")

# scpコマンド
scp_command = 'scp ' + local_filename
scp_command = scp_command + ' ' + ID + '@' + HOST + ':' + DIR + '/' + students_dir + '/' + server_filename

# コマンド実行
command = pexpect.spawn(scp_command)
command.expect('(?i)password')
command.sendline(PASSWORD)
command.expect(pexpect.EOF)

print("SCPコマンドが実行されました")