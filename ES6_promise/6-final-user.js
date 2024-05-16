import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

async function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  try {
    const [userResult, photoResult] = await Promise.allSettled([
      userPromise,
      photoPromise,
    ]);

    return [
      { status: userResult.status, value: userResult.value },
      { status: photoResult.status, value: photoResult.value },
    ];
  } catch (error) {
    console.error("Signup system offline");
    return [];
  }
}

export default handleProfileSignup;
