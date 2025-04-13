{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    # Python with pip
    (python3.withPackages(ps: with ps; [
      pip
      # Add other Python packages you need available globally
    ]))
    
    # Other development tools you might need
    git
  ];

  # Environment variables and setup
  shellHook = ''
    echo "Python development environment activated"
    
    # Create a virtualenv if it doesn't exist
    if [ ! -d "venv" ]; then
      python -m venv venv
      echo "Created new virtual environment in ./venv"
    fi
    
    # Activate the virtualenv
    source venv/bin/activate
    
    # Set up pip to install packages locally
    export PIP_PREFIX="$(pwd)/_build/pip_packages"
    export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"
    export PATH="$PIP_PREFIX/bin:$PATH"
    
    # Install packages from PYBrary.txt if it exists
    if [ -f "PYbrary.txt" ]; then
      echo "Installing packages from PYBrary.txt..."
      pip install -r PYbrary.txt
    else
      echo "Warning: PYbrary.txt file not found"
    fi
  '';
}
