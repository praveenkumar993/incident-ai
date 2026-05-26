const API_URL = import.meta.env.VITE_API_URL


export async function analyzeIncident(file) {

  const formData = new FormData()

  formData.append(
    "file",
    file
  )

  const response = await fetch(

    `${API_URL}/analyze`,

    {
      method: "POST",

      body: formData
    }
  )

  if (!response.ok) {

    throw new Error(
      "Failed to analyze incident"
    )
  }

  return response.json()
}