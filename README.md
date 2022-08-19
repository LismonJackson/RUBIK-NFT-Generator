
<h1><b>RUBIK NFT ART GENERATOR:</b></h1>
<h3>Dependencies:</h3>

<p>Install the latest version of python <a href="https://www.python.org/downloads/">here</a>.</p>

<h3>Usage:</h3>
<br>

```
https://github.com/LismonJackson/RUBIK-NFT-Generator.git

python main.py
```

<h3>Configurations And Customizations:</h3>

<p>Add the amount of NFTs you want to generate. Replace "ETH" with "SOL" for generating NFTs for solana.<p>


```python
Number_Of_NFTS_To_Generate = 50
BlockChain = "ETH"  
```
<p>Give your collection a cool name and brief description.</p>

```python
CollectionName = "Enter your collection name here "
description = "Enter you NFT description here" 
```

<p>Set base URI for your NFT collection</p>

```python
Uri = "ipfs://Replace New Uri Here" 
```
<p>You can order your NFT layers in this section of code.</p>

```python
LayerS_Order = [
    'Background',
    'pants',
    'shirt',
    'shoes',
    'head',
    'access_maskss',
    'accesories_blocks'
]
```

<p>General Metadata for solana</p>

```python
symbol = "SYC"
seller_fee_basis_points = 1000 #Secondary market sales 1000 = 10%
external_url = "https://en.wikipedia.org/wiki/Solana_(blockchain_platform)"
creators = [
    {
        "address": "Add your wallet address here!",
        "share": 100, 
    }
]
```

<p>Extra Metadata for ETH and SOL.</p>

```python
ExtraMetadata = { 
    "compiler": "Rubik v 1.0"
}
```

<p>Duplicate tolerance is for terminating the program, if the number of duplicated generated reaches the tolerance limit. The program is designed to automatically remove duplicates but this features helps the user define the amount of the script should run in order to get the most out of random layer sequences.</p>

```python
DuplicateTolerancee = 1000   # Our Program will end if duplicates are more than 1000
```

<p>Here is a little diagram to help you understand the structure of layer folder tree :</p>

![rubikkk](https://user-images.githubusercontent.com/81759431/185686251-f33fcce6-f5fa-40f7-a84a-f900842caf85.PNG)

<h4>(Note: Only remove or edit the contents inside layer folder. Don't delete or remove it)</h4>
