const updateUniqueItems = (map) => {
  if (!(map instanceof Map)) {
    throw new Error("Cannot process");
  }

  const updatedMap = new Map(map);

  for (const [key, value] of updatedMap.entries()) {
    if (value === 1) {
      updatedMap.set(key, 100);
    }
  }

  return updatedMap;
};

export default updateUniqueItems;
