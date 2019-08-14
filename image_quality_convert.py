import os
from glob import glob
from PIL import Image

def resize(rename, img_quality):
  for dir_name in all_dir:
    #qualityを下げる拡張子を指定
    extensions = ["/*.jpg", "/*.jpeg", "/*.png"]
    files = []
    #リサイズするデータをリストに入れる
    for extension in extensions:
      files.extend(glob(path + dir_name + extension))
    #resize
    for f in files:
      img = Image.open(f)
      #画像サイズを半分にする
      if rename == "はい":
        #ファイル名と拡張子をわける
        ftitle, fext = os.path.splitext(f)
        img.save(ftitle + 'quality' + str(img_quality) + fext, quality=img_quality)
      else:
        img.save(f, quality=img_quality)

#リサイズするフォルダを指定
path = ("./")
#path直下のフォルダ名、ファイル名を取得
all_file = os.listdir(path)
#ファイル名のみにする
all_dir = [f for f in all_file if os.path.isdir(os.path.join(path, f))]

img_quality = int(input("jpgの画像クォリティを1~100で指定してください。(デフォルト75)(95は画質を変えない)>"))
if img_quality < 1 or img_quality > 100:
  inupt("1~100の値を入力してください。処理を終了します。Enterを押してください。")
  sys.exit()

save_name = input("別名保存にしますか？(はい or いいえ)> ")
if save_name == "はい":
  resize(save_name, img_quality)
  input("処理が完了しました。元の名前 + qualityという名前で保存されています。Enterを押してください。")

elif save_name == "いいえ":
  resize(save_name, img_quality)
  input("処理が完了しました。Enterを押してください。")
else:
  input("はい or いいえで入力してください。処理を終了します。Enterを押してください。")

