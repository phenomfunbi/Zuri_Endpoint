from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

current_day = datetime.datetime.utcnow().strftime('%A')
current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

data = {
        'slack_name': 'VICTOR_KEHINDE',
        'current_day': current_day,
        'utc_time': current_utc_time,
        'track' : 'backend',
        'github_file_url' : 'https://github.com/phenomfunbi/Zuri_Endpoint/blob/main/file_name.ext',
        'github_repo_url': 'https://github.com/phenomfunbi/Zuri_Endpoint',
        'status_code': 200
    }

@app.route('/api', methods=['GET'])

def get_details():
     slack_name = request.args.get('slack_name')
     track = request.args.get('track')
     if not slack_name or not track:
          return ('Error: slack_name and track are required'), 400
     else:
         return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
