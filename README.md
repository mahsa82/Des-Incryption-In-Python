<h1>DES Encryption in Python</h1>

This project is a simple implementation of the DES (Data Encryption Standard) encryption algorithm in Python. It uses the pycryptodome library to perform encryption and decryption operations.

**Prerequisites**

Before running the program, you need to install the pycryptodome library:

<pre><code>
  pip install pycryptodome

</code></pre>

**How to Use**
<ol>
<li>Run the main.py file:</li>

<pre><code>
  python main.py
  
</code></pre>


<li>The program will ask whether you want to encrypt (e), decrypt (d), or quit (q).</li>

<li>Enter your message and view the result.</li>
</ol>

**Technical Details**
<ul>
<li>The program uses EAX mode for encryption, which provides high security.</li>

<li>The encryption key is fixed: b'8bytekey'.</li>

<li>For encryption, the message is first converted to bytes and then encrypted using the key and EAX mode.</li>

<li>For decryption, the encrypted data is converted back to bytes and decrypted using the same key and EAX mode.</li>
</ul>

**Note**
<ul>
<li>DES is not secure against modern attacks due to its short key length (56 bits) and is not recommended for sensitive systems.</li>

<li>This project is intended mainly for educational purposes and learning about encryption algorithms.</li>
</ul>
