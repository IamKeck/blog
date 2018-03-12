---
title: DockerでPythonを実行する時の注意点
---
普通に実行させると出力バッファリングが行われるので、docker logsで出力を見ようとしても、
ログが出てこない場合がある。

-uオプションでバッファリングを抑制できる

つまり、例えばDockerfileで

```
CMD ["python", "-u", "実行したいスクリプト"]
```

とすれば良い

### 参考
* <https://docs.python.jp/3/using/cmdline.html#cmdoption-u>
