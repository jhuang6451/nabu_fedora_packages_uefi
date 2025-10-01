[English](../README.md)

# Nabu Fedora 软件包

本仓库包含用于在小米平板5（nabu）上运行 Fedora 的 RPM spec 文件和相关配置。

## 软件包列表

本仓库管理以下软件包：

- `kernel-sm8150`
- `xiaomi-nabu-firmware`
- `nabu-fedora-configs-core`
- `nabu-fedora-configs-extra`
- `nabu-fedora-configs-gnome`
- `nabu-fedora-dualboot-efi`

## 版本与发布流程

本仓库采用一种混合模型进行版本管理和软件包发布，该流程由 GitHub Actions 自动处理。根据版本策略的不同，软件包被分为两大类。

### 软件包分类

#### 1. 自动版本管理包

这些是本仓库作为其代码源的软件包。它们的版本号基于 Git 提交历史自动确定。

- `nabu-fedora-configs-core`
- `nabu-fedora-configs-extra`
- `nabu-fedora-configs-gnome`
- `nabu-fedora-dualboot-efi`

**发布流程:**

1.  **修改代码**：在上述任一软件包的目录中修改文件。
2.  **提交代码**：使用 [Conventional Commits](https://www.conventionalcommits.org/zh-cn/) (约定式提交) 规范来编写提交信息。提交的 `type` 决定了版本的变更：
    - `feat:` 代表新功能，将触发 **MINOR** 版本提升 (例如 `1.1.0` -> `1.2.0`)。
    - `fix:` 代表问题修复，将触发 **PATCH** 版本提升 (例如 `1.1.0` -> `1.1.1`)。
    - 在提交信息的末尾添加 `BREAKING CHANGE:` 将触发 **MAJOR** 版本提升 (例如 `1.1.0` -> `2.0.0`)。
    - 其他类型如 docs, style, refactor, test 等不会触发版本提升。
3.  **推送提交**：将一个或多个提交推送到 `main` 分支。

完成！GitHub Action (`version-and-tag.yml`) 会检测到新的提交，计算出新版本号，并自动推送一个新的软件包标签（例如 `nabu-fedora-configs-core-v1.2.0`）。这个新标签会接着触发 `create-release-tarballs.yml` 工作流，以创建 GitHub Release 并启动 COPR 构建。

#### 2. 手动版本管理包 (跟踪上游)

这些软件包跟踪一个外部的上游代码源。它们的 `Version` (版本) 应与上游版本保持一致，而本地的打包修改则通过 `Release` (发布号) 来跟踪。

- `kernel-sm8150`
- `xiaomi-nabu-firmware`

**发布流程:**

1.  **手动编辑 `.spec` 文件**：在对应软件包的目录中。
    - 若要跟进上游的新版本，请更新 `Version` 字段。
    - 若只是修复本地打包问题，请增加 `Release` 字段的数值。
2.  **更新 `%changelog`**：在 `.spec` 文件中，为您的变更添加一条新的日志。
3.  **提交** 对 `.spec` 文件的修改。
4.  **手动创建并推送 Git 标签**：标签格式需遵循 `[包名]-v[Version号]`。
    ```bash
    # 为新内核版本创建标签的示例
    git tag kernel-sm8150-v6.17.0
    git push origin kernel-sm8150-v6.17.0
    ```
5.  推送这个新标签后，`create-release-tarballs.yml` 工作流会自动被触发，以创建 GitHub Release 并启动 COPR 构建。

### 控制文件

- `release-tarballs.txt`: 列出了本仓库管理的所有软件包目录。
- `.no-auto-version`: 列出了需要从自动化版本流程中排除的软件包（即“手动版本管理包”）。
