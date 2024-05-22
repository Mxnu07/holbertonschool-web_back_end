function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
}

  const studentsByLocation = students.filter((item) => item.location === city);

  return studentsByLocation;

}

export default getStudentsByLocation;
