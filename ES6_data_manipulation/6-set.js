const setFromArray = (arr) => {
  const set = new Set();

  for (const item of arr) {
    try {
      set.add(item);
    } catch (err) {
      throw new Error('Position outside range');
    }
  }

  return set;
};

export default setFromArray;
