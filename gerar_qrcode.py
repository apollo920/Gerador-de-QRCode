import qrcode

#dado paro qrcode
data = "https://www.google.com/search?sca_esv=599792272&sxsrf=ACQVn09r4cq9zkffDNon7fOAyon8o8L7HA:1705672397288&q=meme+de+programador&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiSrt_qzOmDAxWXr5UCHYTiAcQQ0pQJegQIChAB&cshid=1705672419522264&biw=1536&bih=750&dpr=1.25#imgrc=Y2xVElWUqOfKDM"

#objeto qrcode
qr=qrcode.QRCode(version=1,
                 box_size=5,
                 border=5,
                 error_correction=qrcode.constants.ERROR_CORRECT_L)

#adicionar o dado ao qrcode
qr.add_data(data)
qr.make(fit=True)

#Criar img do qrcode
img= qr.make_image(fill_color='black',back_color='white')

#Salvar imagem
img.save("C:/Users/apoll/OneDrive/Área de Trabalho/ICEV - Apollo/projeto-python/img_qrcode/qrcode_meme.png")