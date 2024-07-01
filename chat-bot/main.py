from flask import Flask, render_template, jsonify, request


app = Flask(__name__)


solutions = {
    "wifi": """
        <ul>
            <li>Vérifier que le Wi-Fi est activé sur l'appareil.</li>
            <li>S'assurer que le bon mot de passe Wi-Fi est utilisé.</li>
            <li>Redémarrer le routeur et l'appareil.</li>
            <li>Vérifier que le réseau Wi-Fi est visible et accessible.</li>
            <li>Oublier le réseau Wi-Fi et se reconnecter.</li>
            <li>Mettre à jour les pilotes de la carte réseau.</li>
            <li> Contacter le support IT pour des vérifications supplémentaires.</li>
        </ul>
    """,
    "slow_internet": """
        <ul>
            <li>Vérifier la force du signal Wi-Fi.</li>
            <li>Redémarrer le routeur et l'appareil.</li>
            <li>Fermer les applications qui consomment beaucoup de bande passante.</li>
            <li>Vérifier les interférences avec d'autres appareils électroniques.</li>
            <li>Mettre à jour les pilotes de la carte réseau.</li>
            <li>Contacter le fournisseur d'accès Internet pour vérifier la ligne.</li>
        </ul>
    """,
    "vpn": """
        <ul>
            <li>Vérifier que le logiciel VPN est correctement installé.</li>
            <li>S'assurer que les identifiants de connexion sont corrects.</li>
            <li>Redémarrer l'ordinateur et le routeur.</li>
            <li>Vérifier les mises à jour du logiciel VPN.</li>
            <li>Désactiver temporairement le pare-feu et l'antivirus.</li>
            <li>Contacter le support IT pour des vérifications supplémentaires.</li>
        </ul>
    """,
    "diagnostic_software": """
        <ul>
            <li>Redémarrer l'ordinateur.</li>
            <li>Vérifier les mises à jour du logiciel.</li>
            <li>Réinstaller le logiciel.</li>
            <li>Vérifier les permissions et les droits d'accès.</li>
            <li>Consulter le journal des erreurs pour des messages spécifiques.</li>
            <li>Contacter le support IT pour assistance.</li>
        </ul>
    """,
    "support_du_logiciel": """
    <ul>
            <li>Rechercher l'erreur sur le site de support du logiciel.</li>
            <li>Vérifier les mises à jour et les correctifs.</li>
            <li>Réinstaller le logiciel.</li>
            <li>Contacter le support du fournisseur du logiciel.</li>
            <li>Contacter le support IT pour des vérifications supplémentaires.</li>
        </ul>
    """,
    "diagnostic_qui_ne_fonctionne_pas": """
    <ul>
            <li>Vérifier la connexion Internet.</li>
            <li>Télécharger manuellement la mise à jour depuis le site du fournisseur.</li>
            <li>Désinstaller et réinstaller le logiciel.</li>
            <li>Vérifier les permissions et les droits d'accès.</li>
            <li>Contacter le support IT pour assistance.</li>
        </ul>
    """,
    "printer": """
        <ul>
            <li>Vérifier les connexions câblées.</li>
            <li>Vérifier les niveaux d'encre/papier.</li>
            <li>S'assurer que l'imprimante est allumée et en ligne.</li>
            <li>Mettre à jour les pilotes de l'imprimante.</li>
            <li>Redémarrer l'imprimante et l'ordinateur.</li>
            <li>Contacter le support IT pour assistance.</li>
        </ul>
    """,
    "diagnostic_computer": """
        <ul>
            <li>Vérifier les connexions d'alimentation.</li>
            <li>Essayer une autre prise électrique.</li>
            <li>Vérifier les câbles internes (pour les techniciens).</li>
            <li>Maintenir le bouton d'alimentation enfoncé pendant 10 secondes.</li>
            <li>Contacter le support IT pour des vérifications supplémentaires.</li>
        </ul>
    """,
    "obd_scanner": """
        <ul>
            <li>Vérifier les connexions entre le scanner et le véhicule.</li>
            <li>Redémarrer le scanner et l'ordinateur de diagnostic.</li>
            <li>Mettre à jour le logiciel du scanner.</li>
            <li>Vérifier les manuels pour les codes d'erreur spécifiques.</li>
            <li>Contacter le support IT pour assistance.</li>
        </ul>
    """,
    "malware": """
        <ul>
            <li>Exécuter une analyse complète avec un logiciel antivirus.</li>
            <li>Mettre à jour le logiciel antivirus.</li>
            <li>Désactiver temporairement les extensions de navigateur suspectes.</li>
            <li>Réinitialiser les paramètres du navigateur.</li>
            <li>Contacter le support IT pour assistanc.</li>
        </ul>
    """,
    "secure_connection": """
        <ul>
            <li>Vérifier les paramètres du pare-feu.</li>
            <li>Mettre à jour les certificats de sécurité.</li>
            <li>Réinitialiser les paramètres réseau.</li>
            <li>Utiliser un autre navigateur pour tester la connexion.</li>
            <li>Contacter le support IT pour assistance.</li>
        </ul>
    """,
    "password_reset": """
        <ul>
            <li>Suivre la procédure de réinitialisation sur le site ou l'application concernée.</li>
            <li>Vérifier l'adresse email pour les instructions de réinitialisation.</li>
            <li>Utiliser des réponses aux questions de sécurité si disponibles.</li>
            <li>Contacter le support IT pour assistance.</li>
        </ul>
    """,
    "database_access": """
        <ul>
            <li>Vérifier les permissions et les droits d'accès.</li>
            <li>S'assurer que la connexion réseau est stable..</li>
            <li>Redémarrer l'ordinateur.</li>
            <li>Vérifier les paramètres de connexion à la base de données.</li>
            <li>Contacter le support IT pour assistance.</li>
        </ul>
    """,
    "diagnostic_records": """
        <ul>
            <li>Vérifier les entrées de données pour des erreurs.</li>
            <li>Consulter les journaux d'erreurs de la base de données.</li>
            <li>Exécuter des scripts de correction si disponibles.</li>
            <li>Contacter le support IT pour assistance.</li>
        </ul>
    """,
    "data_backup": """
        <ul>
            <li>Vérifier que les sauvegardes sont régulièrement effectuées.</li>
            <li>Utiliser des outils de récupération de données si nécessaire.</li>
            <li>Vérifier l'intégrité des fichiers de sauvegarde.</li>
            <li>Contacter le support IT pour assistance.</li>
        </ul>
    """,
    "other": """
    <h2>Enter your email and our team will contact you</h2>
    <div id="input-container" class="hidden">
        <form id="input-form" action="/submit" method="POST">
            <input type="text" id="user-input" name="user-input" placeholder="Enter your text here">
            <button type="submit" id="submit-button" onclick="rest()">Submit</button>
        </form>
    </div>
    """,
}


@app.route('/')
def o():
    return render_template('index.html')


@app.route("/send", methods=["POST"])
def send():
    data = request.json
    user_input = data.get("input")
    # Return HTML content
    html_content = solutions[user_input]
    return jsonify({"html": html_content})


@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    user_input = data.get("userInput")
    print('     ')
    # Print received input
    print(f"Received input: {user_input}")

    # Save the user input to a text file
    with open("user_inputs.txt", "a") as file:
        file.write(f"{user_input}\n")

    return jsonify({"status": "success", "userInput": user_input})


if __name__ == "__main__":
    app.run(debug=True)
