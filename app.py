from flask import Flask, request, jsonify

app = Flask(__name__)

students = []


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


@app.route("/students", methods=["POST"])
def register_student():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "name and email are required"}), 400

    if any(s["email"] == data["email"] for s in students):
        return jsonify({"error": "email already registered"}), 409

    student = {
        "id": len(students) + 1,
        "name": data["name"],
        "email": data["email"],
        "course": data.get("course", ""),
    }
    students.append(student)
    return jsonify(student), 201


@app.route("/students/search", methods=["GET"])
def search_students():
    course = request.args.get("course", "").strip()
    if not course:
        return jsonify({"error": "course query parameter is required"}), 400
    if len(course) > 100:
        return jsonify({"error": "course parameter too long"}), 400
    results = [s for s in students if s["course"].lower() == course.lower()]
    return jsonify(results)


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"error": "student not found"}), 404
    return jsonify(student)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
