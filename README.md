# onelinepy
## Python Obfuscator for FUD Python Code.

<img src='oneline.png' />

### Download & Run

```sh
git clone https://github.com/spicesouls/onelinepy
cd onelinepy
python3 -m pip install -r requirements.txt
chmod +x oneline.py
./oneline.py
```

### Usage Guide

<pre>
<b>              _ _                 </b>
<b>  ___ ___ ___| |_|___ ___</b><font color="#FFE82C"><b> ___ _ _</b></font>
<b> | . |   | -_| | |   | -_</b><font color="#FFE82C"><b>| . | | |</b></font><b>     </b><font color="#FFE82C"><b>Python</b></font>
<b> |___|_|_|___|_|_|_|_|___</b><font color="#FFE82C"><b>|  _|_  |</b></font><b>     </b><font color="#729FCF"><b>Obfustucator</b></font>
<b>                         </b><font color="#FFE82C"><b>|_| |___|</b></font>

<b>usage: oneline.py [-h] [-m M] [-i I] [--script SCRIPT] [--code CODE] [--list] [--output OUTPUT]</b>

<b>optional arguments:</b>
<b>  -h, --help       show this help message and exit</b>
<b>  -m M             Obfustucating Method (i.e, -m /one_line/base64)</b>
<b>  -i I             Iterations For Obfustucation.</b>
<b>  --script SCRIPT  File path of Python file to Obfustucate.</b>
<b>  --code CODE      Python code to Obfustucate.</b>
<b>  --list           List Obfustucating Methods.</b>
<b>  --output OUTPUT  Output File.</b>
</pre>

### Examples

```sh
./oneline.py -m /one_line/base64 --script payload.py -i 3
```

```sh
./oneline.py -m /one_line/hex --code "print('HEX!')"
```

### Obfustucation Method List

<pre><b>              _ _                 </b>
<b>  ___ ___ ___| |_|___ ___</b><font color="#FFE82C"><b> ___ _ _</b></font>
<b> | . |   | -_| | |   | -_</b><font color="#FFE82C"><b>| . | | |</b></font><b>     </b><font color="#FFE82C"><b>Python</b></font>
<b> |___|_|_|___|_|_|_|_|___</b><font color="#FFE82C"><b>|  _|_  |</b></font><b>     </b><font color="#729FCF"><b>Obfustucator</b></font>
<b>                         </b><font color="#FFE82C"><b>|_| |___|</b></font>


<b>  Obfustucators ( * = May cause Syntax Errors )</b>
<b> -=============-</b>
<b> 0</b>	<b>/one_line/hex</b>
<b> 1</b>	<b>/one_line/base64</b>
<b> 2</b>	<b>/one_line/base32</b>
<b> 3</b>	<b>/one_line/gunzip*</b>
<b> 4</b>	<b>/one_line/rot13*</b>
<b> 5</b>	<b>/cmd/command</b>
<b> 6</b>	<b>/cmd/powershell</b>
<b> 7</b>	<b>/cmd/powershellhidden</b></pre>
