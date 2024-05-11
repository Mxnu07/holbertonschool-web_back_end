export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  //   name
  get name() {
    return this._name;
  }

  set name(Name) {
    this._name = Name;
  }

  //   length
  get length() {
    return this._length;
  }

  set length(Length) {
    this._length = Length;
  }

  //   students
  get students() {
    return this._students;
  }

  set students(Students) {
    this._students = Students;
  }
}
