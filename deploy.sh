#!/bin/bash
set -Cue
# 以下の環境変数の設定が必要
# AWS_BLOG_PROFILE -> 使用するPROFILE名 
# AWS_BLOG_DISTRIBUTION_ID -> CloudFrontのDistribution ID
PROF_OPT=--profile=${AWS_BLOG_PROFILE}
DIST_ID=${AWS_BLOG_DISTRIBUTION_ID}
stack exec site build
aws s3 sync ./_site/ s3://blog.keckserver.xyz/ --include "*" --acl public-read ${PROF_OPT}
aws cloudfront create-invalidation --distribution-id ${DIST_ID} --paths "/*" ${PROF_OPT}
