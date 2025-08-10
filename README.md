# postmarketOS Ports

Este repositório contém meus ports personalizados do [postmarketOS](https://postmarketos.org) para diferentes dispositivos Android.

Cada port contém arquivos do tipo `device-*` e `linux-*`, compatíveis com a estrutura de `aports` usada pelo `pmbootstrap`.

## 🧩 Dispositivos suportados

| Dispositivo              | Codinome        | Estado     | Interface | Notas |
|--------------------------|------------------|------------|-----------|-------|
| Samsung Galaxy Tab 4 10.1 (SM-T531) | `matisse3g` | 🟡 Em desenvolvimento | Plasma Desktop | Kernel personalizado |
| Motorola Moto G2 (XT1069)          | `titan`     | 🔴 Em espera | Nenhuma ainda | Kernel em construção |

## 📁 Estrutura do repositório

- `samsung-tab4-t531/`: Port para o SM-T531 (matisse3g)
- `motorola-titan/`: Port para o XT1069 (titan)
- `common-scripts/`: Scripts auxiliares genéricos usados nos ports

## ⚙️ Como usar com pmbootstrap

Clone este repositório **fora** da pasta do `pmbootstrap`, depois linke o diretório com:

```sh
pmbootstrap repo init
pmbootstrap repo add device-samsung-matisse3g ~/postmarketos-ports/samsung-tab4-t531/device-samsung-matisse3g
pmbootstrap repo add linux-samsung-matisse3g ~/postmarketos-ports/samsung-tab4-t531/linux-samsung-matisse3g

