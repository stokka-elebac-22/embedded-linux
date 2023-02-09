# Poetry for Raspberry pi (testet og fungerer på armhf):
```bash command-line
sudo apt-get update && sudo apt-get upgrade
sudo apt install python3-distutils python3-dev libssl-dev libffi-dev
```
## Fungerer uten Rust på arm64, for armhf må en også kjøre (før poetry install):
(men, rust er jo fint uansett)
```bash command-line
curl https://sh.rustup.rs/ -sSf | sh
export PATH=$PATH:~/.cargo/bin
```
## Fullfører installasjon av poetry med:
```bash command-line
curl -sSL https://install.python-poetry.org/ | python3 -
export PATH="/home/asbjorn/.local/bin:$PATH" 
```

OpenCV er enklest å installere på arm64
