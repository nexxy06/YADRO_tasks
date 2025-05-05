# Задачи от Радиочастотных систем
1. Linux команды 
```bash
echo "Hello, DevOps!" | tee ~/hello.txt
``` 
2. Linux команды 
```bash
grep "status" /var/log/dpkg.log | head -n 5
``` 
3. Bash скрипт  
Запишу данные в файл:
```bash
tee config.txt <<EOF
name: test server
path: /home/user/data
file: data.txt
port: 8080
log path: /var/log/app
EOF
``` 
Сам bash скрипт:
```bash
#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file_to_search> <parameter>"
    exit 1
fi

real_path="$(realpath "$1")"

grep "$2" $real_path

```

4. Dockerfile оптимизация:  
см. Dockerfile
