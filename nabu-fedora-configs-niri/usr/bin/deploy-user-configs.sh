%post
# +------------------------------------------------------------------------+
# |                                                                        |
# |      将 /etc/skel 中的配置文件复制到现有用户的主目录（不覆盖）         |
# |                                                                        |
# +------------------------------------------------------------------------+
# |                                                                        |
# |  描述：                                                                |
# |  此脚本旨在将 /etc/skel 目录中的默认配置文件部署到系统中所有现有        |
# |  （非系统）用户的主目录中。它会智能地跳过任何已经存在的文件，          |
# |  确保不会覆盖用户现有的自定义配置。                                    |
# |                                                                        |
# |------------------------------------------------------------------------+
# |                                                                        |
# |  工作流程：                                                            |
# |  1. 动态获取 /etc/skel 目录下的所有文件的相对路径列表。                |
# |  2. 识别系统上 UID 大于或等于 1000 的所有用户的主目录。                |
# |  3. 遍历每个用户的主目录。                                             |
# |  4. 对于每个用户，遍历配置文件列表。                                   |
# |  5. 检查目标路径（在用户的主目录中）是否已存在文件。                   |
# |  6. 如果目标文件不存在，则复制文件并设置正确的所有权。                 |
# |  7. 如果目标文件已存在，则跳过。                                       |
# |                                                                        |
# +------------------------------------------------------------------------+

# 遍历所有 UID >= 1000 的普通用户
getent passwd | awk -F: '$3 >= 1000 {print $1, $6}' | while read -r username user_home; do
    # 检查主目录是否存在且可写
    if [ -d "${user_home}" ] && [ -w "${user_home}" ]; then
        echo "Processing user '${username}' in home directory: ${user_home}"

        # 动态查找 /etc/skel 中的所有文件，并获取它们的相对路径
        # 'cd' 和 'find .' 的组合可以轻松地获得相对路径
        (cd /etc/skel && find . -type f) | while IFS= read -r skel_file_rel; do
            # 移除开头的 './'
            skel_file_rel="${skel_file_rel#./}"

            source_file="/etc/skel/${skel_file_rel}"
            dest_file="${user_home}/${skel_file_rel}"

            # 检查目标文件是否已经存在
            if [ -e "${dest_file}" ]; then
                echo "  -> Exists, skipping: ${dest_file}"
            else
                echo "  -> Missing, copying to: ${dest_file}"
                # 创建目标目录，以防万一
                mkdir -p "$(dirname "${dest_file}")"
                # 复制文件
                cp "${source_file}" "${dest_file}"
                # 更改文件的所有者和组，以匹配用户
                chown "${username}:${username}" "${dest_file}"
            fi
        done
        echo "--------------------------------------------------"
    else
        echo "Skipping user '${username}', home directory not found or not writable: ${user_home}"
    fi
done

echo "Post-install script finished."