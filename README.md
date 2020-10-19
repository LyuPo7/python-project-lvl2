# python-project-lvl2

<a href="https://codeclimate.com/github/LyuPo7/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/b068d8adf854428f2f41/maintainability" /></a> <a href="https://codeclimate.com/github/LyuPo7/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/b068d8adf854428f2f41/test_coverage" /> </a><a href="https://travis-ci.org/LyuPo7/python-project-lvl2"><img src="https://travis-ci.org/LyuPo7/python-project-lvl2.svg?branch=master"></a> ![Python package](https://github.com/LyuPo7/python-project-lvl2/workflows/Python%20package/badge.svg)

<h3>Project Description:</h3>
    <p>Generate difference utility</p>
    <ul>
        <li>Works with 2 types files: <b>.json, .yaml</b>;</li>
        <li>Works with nested files;</li>
        <li>Supports 3 different formats for output.</li>
    </ul>

<h3>Installation:</h3>
    <p>for install type in command line:</p>
        <i>python3 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple lyupo7-gendiff</i>

<h3>How to use?</h3>
    <p>Use <b>gendiff</b> command with appropriate keys.</p>
    <p><i>(More information in asciinemas below)</i></p>

<h4>Compare json files</h4>
    <p>gendiff 'path2file1' 'path2file2'</p>
    <a href="https://asciinema.org/a/362104" target="_blank"><img src="https://asciinema.org/a/362104.svg" /></a>

<h4>Compare yaml files</h4>
    <p>gendiff 'path2file1' 'path2file2'</p>
    <a href="https://asciinema.org/a/362105" target="_blank"><img src="https://asciinema.org/a/362105.svg" /></a>

<h4>Compare recursive files</h4>
    <p>gendiff 'path2file1' 'path2file2'</p>
    <a href="https://asciinema.org/a/362106" target="_blank"><img src="https://asciinema.org/a/362106.svg" /></a>

<h4>Compare files with plaintext output</h4>
    <p>gendiff -f plain 'path2file1' 'path2file2'</p>
    <a href="https://asciinema.org/a/362107" target="_blank"><img src="https://asciinema.org/a/362107.svg" /></a>

<h4>Compare files with json output</h4>
    <p>gendiff -f json 'path2file1' 'path2file2'</p>
    <a href="https://asciinema.org/a/362108" target="_blank"><img src="https://asciinema.org/a/362108.svg" /></a>
