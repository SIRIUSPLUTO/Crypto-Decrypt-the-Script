#二维码解码
def qr_decode():
    """
    二维码解码

    :return:
    """
    import zxing

    reader = zxing.BarCodeReader()
    barcode = reader.decode('/home/QR_code.png')
    print(barcode.parsed)
