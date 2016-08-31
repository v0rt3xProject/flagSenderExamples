#!/bin/bash

# Configuration
FLAG_SERVER=${FLAG_SERVER:-"10.0.0.10"}

FLAG_TCP_HI_PORT=${FLAG_TCP_HI_PORT:-6666}
FLAG_TCP_NO_PORT=${FLAG_TCP_NO_PORT:-5555}
FLAG_TCP_LO_PORT=${FLAG_TCP_LO_PORT:-4444}

FLAG_HTTP_PORT=${FLAG_HTTP_PORT:-9999}

FLAG_HI_URL=${FLAG_HI_URL:-"http://${FLAG_SERVER}:${FLAG_HTTP_PORT}/flag/hi"}
FLAG_NO_URL=${FLAG_NO_URL:-"http://${FLAG_SERVER}:${FLAG_HTTP_PORT}/flag/no"}
FLAG_LO_URL=${FLAG_LO_URL:-"http://${FLAG_SERVER}:${FLAG_HTTP_PORT}/flag/lo"}

FLAG_JSON_STATUS_URL=${FLAG_JSON_STATUS_URL:-"http://${FLAG_SERVER}:${FLAG_HTTP_PORT}/flag/status.json"}

# Helper Functions
function tcp_send() {
  case $1 in
    hi)
      SEND_PORT=${FLAG_TCP_HI_PORT}
    ;;
    no)
      SEND_PORT=${FLAG_TCP_NO_PORT}
    ;;
    lo)
      SEND_PORT=${FLAG_TCP_LO_PORT}
    ;;
    *)
      SEND_PORT=${FLAG_TCP_HI_PORT}
    ;;
  esac

  shift

  IFS=$' '
  for flag in "$@"; do
      echo "${flag}" | nc ${FLAG_SERVER} ${SEND_PORT}
  done
}

function http_send() {
  case $1 in
    hi)
      SEND_URL=${FLAG_HI_URL}
    ;;
    no)
      SEND_URL=${FLAG_NO_URL}
    ;;
    lo)
      SEND_URL=${FLAG_LO_URL}
    ;;
    *)
      SEND_URL=${FLAG_HI_URL}
    ;;
  esac

  shift

  IFS=$' '
  for flag in "$@"; do
      echo "${flag}: $(echo \"${flag}\" | curl -sSL \"${SEND_URL}/${flag}\" 2> /dev/null)"
  done
}

# Main Program

tcp_send hi "0123456789abcdef01234596789abcdef="
http_send hi "0123456789abcdef01234596789abcdef="
