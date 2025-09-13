%undefine        _debugsource_packages
%global tag      6.16
Version:         6.16.0
Release:         1.sm8150%{?dist}
ExclusiveArch:   aarch64
Name:            kernel-sm8150
Summary:         The Linux kernel for sm8150 devices
License:         GPLv2
URL:             https://gitlab.com/sm8150-mainline/linux
Source0:         %{url}/-/archive/sm8150/%{tag}/linux-sm8150-%{tag}.tar.gz
Source1:         extra-sm8150.config

# 确保构建环境中包含 dracut 用于生成 initramfs
# kernel-install 工具由 systemd 包提供，通常已存在于标准构建环境中
BuildRequires:   bc bison dwarves diffutils elfutils-devel findutils gcc gcc-c++ git-core hmaccalc hostname make openssl-devel perl-interpreter rsync tar which flex bzip2 xz zstd python3 python3-devel python3-pyyaml rust rust-src bindgen rustfmt clippy opencsd-devel net-tools dracut

Provides:        kernel               = %{version}-%{release}
Provides:        kernel-core          = %{version}-%{release}
Provides:        kernel-modules       = %{version}-%{release}
Provides:        kernel-modules-core  = %{version}-%{release}

%global uname_r %{version}-%{release}.%{_target_cpu}

%description
Mainline kernel for sm8150 (Qualcomm Snapdragon 855/860) devices, packaged for standard Fedora systems with UEFI boot support.

%prep
%autosetup -n linux-sm8150-%{tag}

# 准备默认配置
make defconfig sm8150.config

%build
# 移除既有的 CONFIG_LOCALVERSION，我们将通过 make 命令的参数来控制它
sed -i '/^CONFIG_LOCALVERSION=/d' .config
# 追加额外的配置
cat %{SOURCE1} >> .config
# 确保没有 localversion 文件影响版本号
rm -f localversion*

make olddefconfig
# 使用 EXTRAVERSION 和空的 LOCALVERSION 来精确构建内核版本号
make EXTRAVERSION="-%{release}.%{_target_cpu}" LOCALVERSION= -j%{?_smp_build_ncpus} Image modules dtbs

%install

# 1. 安装内核模块
# INSTALL_MOD_PATH 指向 %{buildroot}/usr，这会将模块安装到 %{buildroot}/usr/lib/modules/%{uname_r}/
make EXTRAVERSION="-%{release}.%{_target_cpu}" LOCALVERSION= \
     INSTALL_MOD_PATH=%{buildroot}/usr \
     modules_install

# 2. 安装内核镜像、System.map 和配置文件到 /boot 目录
# 这是标准 Fedora 的做法，文件会带有版本号后缀
install -Dm644 arch/arm64/boot/Image %{buildroot}/boot/vmlinuz-%{uname_r}
install -Dm644 System.map %{buildroot}/boot/System.map-%{uname_r}
install -Dm644 .config    %{buildroot}/boot/config-%{uname_r}

# 3. 安装设备树文件 (DTB)
# kernel-install 会自动在 /usr/lib/modules/%{uname_r}/dtb/ 路径下寻找 DTB 文件
install -d %{buildroot}/usr/lib/modules/%{uname_r}/dtb/qcom
install -Dm644 arch/arm64/boot/dts/qcom/sm8150-xiaomi-nabu.dtb %{buildroot}/usr/lib/modules/%{uname_r}/dtb/qcom/sm8150-xiaomi-nabu.dtb


%files
/boot/vmlinuz-%{uname_r}
/boot/System.map-%{uname_r}
/boot/config-%{uname_r}
/usr/lib/modules/%{uname_r}


%posttrans
set -e
uname_r=%{uname_r}

# 1. 为新内核生成模块依赖
depmod -a "${uname_r}"

# 2. 使用 dracut 生成 initramfs，并直接放置在 /boot 目录下
dracut -v --force "/boot/initramfs-${uname_r}.img" "${uname_r}"

# 3. 使用 kernel-install 工具添加新内核
# 这是在现代 Fedora 系统上管理内核安装的推荐方法。
# 它会自动处理引导加载程序的配置（如 systemd-boot 或 grub2），
# 并将需要的文件（内核、initramfs、DTB）复制到 ESP 分区（/boot/efi）中（如果引导加载程序需要）。
kernel-install add "${uname_r}" "/boot/vmlinuz-${uname_r}"

%postun
# 这个脚本在卸载包时运行
if [ "$1" -eq 0 ] ; then
    # 使用 kernel-install 移除此内核的引导项，保持系统清洁
    kernel-install remove %{uname_r}
fi

%changelog
* Sat Sep 13 2025 jhuang6451 <xplayerhtz123@outlook.com> - 6.16.0-1.sm8150
- Modified spec for standard Fedora systems, removing ostree logic.
- Adopted standard file paths (/boot) and kernel-install for UEFI/bootloader integration.

* Fri Sep 12 2025 jhuang6451 <xplayerhtz123@outlook.com> - 6.16.0-0.sm8150
- Added post-transaction script to copy kernel and DTB to ESP for UEFI boot.

* Fri Jul 25 2025 gmanka 6.16.0
- update to 6.16.0