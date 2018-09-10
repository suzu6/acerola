# README

## センサ

- [bme280](https://deviceplus.jp/hobby/raspberrypi_entry_039/)

## 物品

- [Raspberry Pi 3B+](https://www.amazon.co.jp/gp/product/B01N216X19/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=suzu60c-22&creative=1211&linkCode=as2&creativeASIN=B01N216X19&linkId=z7b5638deb81af5805803e8dc94cfdez) ２個
- [USB 扇風機](https://www.amazon.co.jp/gp/product/B0759PHDYB/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=suzu60c-22&creative=1211&linkCode=as2&creativeASIN=B0759PHDYB&linkId=e29aa91f470f798d2ad7478cad9d8f91) １個
- [USB ライト 白](https://www.amazon.co.jp/gp/product/B0727PXH9Z/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=suzu60c-22&creative=1211&linkCode=as2&creativeASIN=B0727PXH9Z&linkId=123da26d79e6ba12c36f689caa45146c) １個
- [USB ライト 青](https://www.amazon.co.jp/gp/product/B06Y59VY9F/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=suzu60c-22&creative=1211&linkCode=as2&creativeASIN=B06Y59VY9F&linkId=243491fdbc875b3ca2ad2d3e66e5c42f) １個

## power control of USB hub


[uhubctl](https://github.com/mvp/uhubctl)


```sh
# port 1 off
uhubctl -p 1 -a 0
# port 2 on
uhubctl -p 2 -a 1
```

## run shell from python 

python -v 2.7

シェルの実行には、[commands](https://docs.python.jp/2/library/commands.html)もしくは[subprocess](https://docs.python.jp/2/library/subprocess.html#module-subprocess)を使う。


```sh
#!/usr/bin/env python

import commands

check = commands.getoutput("./ip-address_check.sh 192.168.1.1")

print check
```


## 参考

- [Raspberry Pi の USB ポートを制御する２](https://blog.withachristianwife.com/2018/03/27/controlling-usb-port-on-pi-2/)
- [pythonで外部のシェルスクリプトやコマンドを実行する方法](https://qiita.com/komeiy/items/d6b5f25bf1778fa10e21)


## censor

温度センサ　BME280

i2cのセットアップ

```sh
$ sudo raspi-config
```
コンフィグを立ち上げてから、以下の順序でオプションを選択します。

1. 5 Interfacing Options
1. P5 I2C 
1. <Yes>

「The ARM I2C interface is enabled」と表示されたらOK。

設定を反映させるため、再起動します。
```
$ sudo reboot
```

### i2c-toolsをインストール

```sh
# コマンドから確かめる用
$ sudo apt-get install i2c-tools
$ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- 76 --
```


```
# pythonのモジュール
$ pip install smbus2
```

[smbus2 python2.7のサンプルコード](https://github.com/SWITCHSCIENCE/BME280/blob/master/Python27/bme280_sample.py)

[第39回「ラズベリーパイで温度・湿度・気圧をまとめて取得！AE-BME280でIC2通信」](https://deviceplus.jp/hobby/raspberrypi_entry_039/)
[RaspberryPiではじめてのI2C通信〜温度計測編〜](https://qiita.com/kamujun/items/51f85339bfd582b27752)

## setup

$ pyenv virtualenv 3.6.5 acelora-env
$ pyenv local acelora-env