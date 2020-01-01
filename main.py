from flask import Flask, render_template, request
from VIC import *
from modul_stepkos import *
from cezaworking import *
import os
import io

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'files')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True


@app.route("/encrypt_file", methods=['POST'])
def encrypt():
     latestfile = request.files['user_file']
     full_filename = os.path.join(app.config['UPLOAD_FOLDER'], latestfile.filename)
     latestfile.save(full_filename)
     option = request.form['options']
     if option == 'szyfr_vic':
         with open(full_filename, "r", encoding="utf-8") as file:
             with open(os.path.join(UPLOAD_FOLDER, 'encrypted_file.txt'), "w", encoding="utf-8") as file_to_write:
                 for line in file.readlines():
                     file_to_write.write(VIC.encrypt(line))
     if option == 'szyfr_vigenere':
         with open(full_filename, "r", encoding="utf-8") as file:
             with open(os.path.join(UPLOAD_FOLDER, 'encrypted_file.txt'), "w", encoding="utf-8") as file_to_write:
                 for line in file.readlines():
                     file_to_write.write(Vigenere.encrypt("kghr",line))
     if option == 'cezar':
        with open(full_filename, "r", encoding="utf-8") as file:
            with open(os.path.join(UPLOAD_FOLDER, 'encrypted_file.txt'), "w", encoding="utf-8") as file_to_write:
                for line in file.readlines():
                    file_to_write.write(cezar.szyfruj(line)) 
     return render_template('download.html', method="encrypt", filename="encrypted_file.txt")

@app.route("/decrypt_file", methods=['POST'])
def decrypt():
     latestfile = request.files['user_file']
     full_filename = os.path.join(app.config['UPLOAD_FOLDER'], latestfile.filename)
     latestfile.save(full_filename)
     option = request.form['options']
     if option == 'szyfr_vic':
         with open(full_filename, "r", encoding="utf-8") as file:
             with open(os.path.join(UPLOAD_FOLDER, 'decrypted_file.txt'), "w", encoding="utf-8") as file_to_write:
                 for line in file.readlines():
                     file_to_write.write(VIC.decrypt(line))
     if option == 'szyfr_vigenere':
         with open(full_filename, "r", encoding="utf-8") as file:
             with open(os.path.join(UPLOAD_FOLDER, 'decrypted_file.txt'), "w", encoding="utf-8") as file_to_write:
                 for line in file.readlines():
                     file_to_write.write(Vigenere.decipher("kghr",line))
     if option == 'cezar':
        with open(full_filename, "r", encoding="utf-8") as file:
            with open(os.path.join(UPLOAD_FOLDER, 'decrypted_file.txt'), "w", encoding="utf-8") as file_to_write:
                for line in file.readlines():
                    file_to_write.write(cezar.deszyfruj(line)) 
     return render_template('download.html', method="decrypt", filename="decrypted_file.txt")

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")
 
if __name__ == "__main__":
    app.run(host='127.0.0.1',port="8000")