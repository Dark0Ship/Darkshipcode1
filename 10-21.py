saveFp=asksaveasfile(parent=window,mode="w",defaultextension=".jpg",
                     fieltypes=(("JPG 파일","*.jpg;*,jpeg"),("모든 파일","*.*")))
label1.configure(text=saveFp)
saveFp.close()
