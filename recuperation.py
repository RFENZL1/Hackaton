from flask import Flask, request, render_template
import speechRecognition

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
        
        print(request.method)
        if request.method == 'POST':
        # Récupérez le fichier uploadé
            uploaded_file = request.files['audio-file']
            print(uploaded_file.filename)
        # Vérifiez si un fichier a été uploadé
            if uploaded_file:
            # Faites quelque chose avec le fichier, par exemple, enregistrez-le sur le serveur
                uploaded_file.save(uploaded_file.filename)

            # Vous pouvez également accéder à d'autres informations du formulaire si nécessaire
            # Par exemple, request.form['nom_du_champ']
            # print(request.form)
            # return  uploaded_file 

    # Pour la méthode GET, renvoyer simplement le formulaire HTML
            result = speechRecognition.speechRecognition.music(uploaded_file.filename)
            print(result)           
            return render_template('index.html', data=result)
        return render_template("index.html")

if __name__ == '__main__':
    app.run()