from flask import Flask, jsonify, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
from logger import init_logger

app= Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application Todo Info', version='1.0.0')
logger=init_logger()
@app.route('/')
def index():
    logger.info('Get /')
    return render_template('index.html')


@app.route('/log_task', methods=['POST'])
def log_task():
    try:
        data = request.get_json()  # Safely get JSON data from request
        task_text = data.get('taskText')  # Extract taskText field
        if task_text:  # Check if taskText is provided
            logger.info(f'Item added: {task_text} - Post /log_task')  # Log the task addition
            return jsonify({"message": "Task logged successfully"}), 200
        else:
            return jsonify({"error": "No taskText provided"}), 400
    except Exception as e:
        logger.error(f'Error logging task: {str(e)}')  # Log any errors
        return jsonify({"error": "Failed to log task"}), 500

if __name__=='__main__':
    app.run('0.0.0.0',5000)

