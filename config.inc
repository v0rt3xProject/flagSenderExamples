export FLAG_SERVER="10.0.0.10"

export FLAG_TCP_HI_PORT=6666
export FLAG_TCP_NO_PORT=5555
export FLAG_TCP_LO_PORT=4444

export FLAG_HTTP_PORT=9999

export FLAG_HI_URL="http://${FLAG_SERVER}:${FLAG_HTTP_PORT}/flag/hi"
export FLAG_NO_URL="http://${FLAG_SERVER}:${FLAG_HTTP_PORT}/flag/no"
export FLAG_LO_URL="http://${FLAG_SERVER}:${FLAG_HTTP_PORT}/flag/lo"

export FLAG_JSON_STATUS_URL="http://${FLAG_SERVER}:${FLAG_HTTP_PORT}/flag/status.json"
