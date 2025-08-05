#!/bin/sh
#
# Script para aplicar o .config correto no diretório de build do kernel
# Reutilizável para múltiplos dispositivos com arquivos config-*.armv7
# Usado no prepare() do APKBUILD
#
# Uso esperado:
#   sh "$startdir"/../../common-scripts/atualizar_config_kernel.sh

set -e

# Detecta o nome do arquivo de configuração automaticamente
CONFIG=$(find "$startdir" -maxdepth 1 -type f -name "config-*.armv7" | head -n1)
KERNEL_DIR=$(find "$srcdir" -maxdepth 1 -type d -name "linux-*")

if [ ! -f "$CONFIG" ]; then
    echo "Erro: Arquivo de configuração *.armv7 não encontrado em $startdir"
    exit 1
fi

if [ ! -d "$KERNEL_DIR" ]; then
    echo "Erro: Diretório do kernel linux-* não encontrado em $srcdir"
    exit 1
fi

echo "Copiando $(basename "$CONFIG") para $KERNEL_DIR/.config"
cp "$CONFIG" "$KERNEL_DIR/.config"
