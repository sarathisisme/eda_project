# EDA for king county dataset

Please follow instructions below for the setup. After the setup you can use the two jupyter notebooks for EDA:
- Hypotheses_EDA.ipynb : Contains the EDA to support the three hypotheses that we have formulated
- Client_EDA.ipynb : Contains the EDA required to make 3 recommendations to help our client

Final results of the EDA can be found in:
- EDA_Presentation_final.pdf : presentation
- All the result images can be found in folder images/


## Requirements

- pyenv
- python==3.11.3

## Setup

## MAC 

 Install the virtual environment and the required packages by following commands:

    ```
    pyenv local 3.11.3
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`WindowsOS`** type the following commands :


- `Step_1:` Update Chocolatey and install Node by following commands:
    ```sh
    choco upgrade chocolatey
    choco install nodejs
    ```

- `Step_2:` Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :
  
    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
 

 **`Note:`**
    If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:

   ```Bash
   python.exe -m pip install --upgrade pip
   ```
