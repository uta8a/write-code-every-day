# 2021-01-04
- terraform backend S3用のcloudformationを書いた。
- https://www.terraform.io/docs/backends/types/s3.html#multi-account-aws-architecture
  - これによると、tfstateをS3で管理するならS3を立ち上げるのはそのterraformの範囲外であるべきと書かれている。
  - そのためCFnを使うことにした。
- はまったこと
  - ``aws cloudformation ... --template-body <ここ>``で、ここ部分には``file:///``からはじまるフルパスを入れる必要があった。これがないと、invalidみたいなのが出るだけで、ファイルがないよとは教えてくれないので注意
  - 権限が足りない
    - CFn, S3の権限が必要(書き込みが必要なので強めの権限になる)
  - yamlのネストで失敗
    - YAML難しい。 https://github.com/widdix/aws-cf-templates/blob/master/state/s3.yaml と見比べて解決したので、ある程度ドキュメント読んだら例を探しに行くとよい。
