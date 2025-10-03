#!/bin/bash

# 如果任何命令失败，立即退出脚本
set -e

# --- 脚本开始 ---
echo "--> Installing copr-cli..."
dnf install -y copr-cli

echo "--> Configuring copr-cli authentication..."
mkdir -p ~/.config
# 使用环境变量配置 copr-cli
cat <<EOF > ~/.config/copr
[copr-cli]
login = $COPR_LOGIN
username = $COPR_USERNAME
token = $COPR_TOKEN
copr_url = $COPR_URL
EOF

echo "--> Verifying copr identity..."
copr-cli whoami

# 这些变量将由 GitHub Actions 的 env 上下文提供
# 例如：CLONE_URL, COMMITTISH, SUBDIRECTORY, SPEC, COPR_REPO
echo "--> Triggering Copr build in repo '${COPR_REPO}' for package '${SUBDIRECTORY}'..."
copr-cli buildscm \
  --clone-url "${CLONE_URL}" \
  --commit "${COMMITTISH}" \
  --subdir "${SUBDIRECTORY}" \
  --spec "${SPEC}" \
  --type git \
  --method rpkg \
  --nowait \
  "${COPR_REPO}"

echo "--> Copr build triggered successfully for ${SUBDIRECTORY}."