# NGINX流媒体访问限制

限制单个IP能发起的连接：limit_conn addr 1;

限制视频速率：limit_rate 1024k;

刷新nginx：nginx -s reload

nginx.conf

```
server {
    listen 80;
    server_name localhost;
    location / {
        root html;
        index index.html index.htm;
        proxy_pass http://movie;
    }
        location ~ \.flv$ {
        mp4;
        limit_conn addr 1;
        limit_rate 1024k;
        rewrite ^/static/uploads/(.+?).flv$ /movie/app/static/uploads/$1.flv permanent;
	}
    location ~ \.mp4$ {
        mp4;
        limit_conn addr 1;
        limit_rate 1024k;
        rewrite ^/static/uploads/(.+?).mp4$ /movie/app/static/uploads/$1.mp4 permanent;
	}
	error_page 500 502 503 504 /50x.html;
	location = /50x.html {
        root html;
	}
}

```

