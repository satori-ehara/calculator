# Tkinterライブラリのインポート
import tkinter
import math

state = 0
number_X = 25
number_Y = 70
cnt = 1

number = 0
number_dash = 0
PMMD = "no"

def check_state():
  global state
  if state == 1:
    txtBox.delete(0, tkinter.END)
    state = 0

def output_number(number):
  txtBox.configure(state='normal')
  txtBox.delete(0, tkinter.END)
  txtBox.insert(tkinter.END,number)
  txtBox.configure(state='readonly')

# click時のイベント
def btn_click(event):
  str = event.widget["text"]
  print(str)
  txtBox.configure(state='normal')
  global PMMD

  if float(txtBox.get()) == 0 : # 表示盤面が0の時は0を削除して押されたボタンの数字を表示
    if "." in txtBox.get() : #0でも 0. となっている場合は削除せず。
      print("ダメ")
    else :
      txtBox.delete(0, tkinter.END) #全消し

  check_state()

  txtBox.insert(tkinter.END,str)
  txtBox.configure(state='readonly')
  print(float(txtBox.get()))

def btn_c(event):
  txtBox.configure(state='normal')
  txtBox.delete(0, tkinter.END)
  txtBox.insert(tkinter.END,0)
  txtBox.configure(state='readonly')

def btn_dt(event):
  txtBox.configure(state='normal')
  if "." in txtBox.get() : # テキストに.が含まれない場合にのみ.を追加
    print("ダメ")
  else :
    txtBox.insert(tkinter.END,".")
  txtBox.configure(state='readonly')

def btn_plus(event):
  print("push plus")
  global PMMD,state,number
  if PMMD != "no": #四則演算中であれば計算結果を算出
    number = get_math(PMMD,number)
    output_number(number)

  PMMD = "plus"
  number = float(txtBox.get())
  state = 1
  print(number)
  print(PMMD)

def btn_minus(event):
  global PMMD,state,number
  if PMMD != "no": #四則演算中であれば計算結果を算出
    number = get_math(PMMD,number)
    output_number(number)

  PMMD = "minus"
  number = float(txtBox.get())
  state = 1
  print("push minus")

def btn_multiplied(event):
  global PMMD,state,number
  if PMMD != "no": #四則演算中であれば計算結果を算出
    number = get_math(PMMD,number)
    output_number(number)

  PMMD = "multiplied"
  number = float(txtBox.get())
  state = 1
  print("push multiplied")

def btn_divided(event):
  global PMMD,state,number
  if PMMD != "no": #四則演算中であれば計算結果を算出
    number = get_math(PMMD,number)
    output_number(number)

  PMMD = "divided"
  number = float(txtBox.get())
  state = 1
  print("push divided")

def btn_equal(event):
  global PMMD,number
  print("push equal")
  if PMMD != "no" : #四則演算中であれば計算結果を算出
    number = get_math(PMMD,number)
  
  print(number)
  output_number(number)
  PMMD = "no"

def get_math(PMMD,numver):
  print("状態は" + PMMD)
  math = 0
  if PMMD == "plus":
    math = number + float(txtBox.get())
  elif PMMD == "minus":
    math = number - float(txtBox.get())
  elif PMMD == "multiplied":
    math = number * float(txtBox.get())
  elif PMMD == "divided":
    math = number / float(txtBox.get())

  if math - int(math) == 0 :#小数点以下が0の場合intで表示
    return int(math)
  else :
    return math




# 画面作成
tki = tkinter.Tk()
tki.geometry('220x200') # 画面サイズの設定
tki.title('電卓テスト') # 画面タイトルの設定

txtBox = tkinter.Entry(justify='right')
txtBox.configure(state='readonly', width=26)
txtBox.place(x=20, y=10)
txtBox.configure(state='normal')
txtBox.insert(tkinter.END,0)
txtBox.configure(state='readonly')


# ボタンの作成
while cnt<10 : #1~9
    Y = (math.ceil(cnt/3) - 1) * 30 + number_Y
    X = ((cnt-1)%3) * 40 + number_X
    btn = tkinter.Button(tki, text=cnt,width=3)
    btn.bind("<1>",btn_click)
    btn.place(x=X, y=Y) #ボタンを配置する位置の設定
    cnt += 1

btn = tkinter.Button(tki, text="C",width=3) #Cボタン
btn.bind("<1>",btn_c)
btn.place(x=number_X, y=number_Y-30) #ボタンを配置する位置の設定

btn = tkinter.Button(tki, text=0,width=3) #０ボタン
btn.bind("<1>",btn_click)
btn.place(x=number_X+40, y=number_Y+90) #ボタンを配置する位置の設定

btn = tkinter.Button(tki, text=".",width=3) #.ボタン
btn.bind("<1>",btn_dt)
btn.place(x=number_X+80, y=number_Y+90) #ボタンを配置する位置の設定

btn = tkinter.Button(tki, text="+",width=3) # ＋ボタン
btn.bind("<1>",btn_plus)
btn.place(x=number_X+120, y=number_Y-30) #ボタンを配置する位置の設定

btn = tkinter.Button(tki, text="-",width=3) # ―ボタン
btn.bind("<1>",btn_minus)
btn.place(x=number_X+120, y=number_Y) #ボタンを配置する位置の設定

btn = tkinter.Button(tki, text="×",width=3) # ×ボタン
btn.bind("<1>",btn_multiplied)
btn.place(x=number_X+120, y=number_Y+30) #ボタンを配置する位置の設定

btn = tkinter.Button(tki, text="÷",width=3) # ÷ボタン
btn.bind("<1>",btn_divided)
btn.place(x=number_X+120, y=number_Y+60) #ボタンを配置する位置の設定

btn = tkinter.Button(tki, text="＝",width=3) # =ボタン
btn.bind("<1>",btn_equal)
btn.place(x=number_X+120, y=number_Y+90) #ボタンを配置する位置の設定


# 画面をそのまま表示
tki.mainloop()