{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.pip
    python3Packages.virtualenv
    mysql
    libmysqlclient
    pkg-config
  ];

  shellHook = ''
    # Création et activation de l'environnement virtuel
    if [ ! -d ".venv" ]; then
      python3 -m venv .venv
    fi
    source .venv/bin/activate
    
    # Installation des dépendances
    pip install -r PYbrary.txt
  '';
}
