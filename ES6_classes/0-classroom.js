export default class ClassRoom {
  constructor(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize;
    this._students = [];
  }

  get maxStudentsSize() {
    return this._maxStudentsSize;
  }

  get students() {
    return this._students;
  }

  addStudent(student) {
    if (this._students.length < this._maxStudentsSize) {
      this._students.push(student);
      console.log(`Student ${student} added to the classroom.`);
    } else {
      console.log("Classroom is full, cannot add more students.");
    }
  }

  removeStudent(student) {
    const index = this._students.indexOf(student);
    if (index !== -1) {
      this._students.splice(index, 1);
      console.log(`Student ${student} removed from the classroom.`);
    } else {
      console.log(`Student ${student} not found in the classroom.`);
    }
  }

  getStudentCount() {
    return this._students.length;
  }
}
