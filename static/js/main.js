document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('generate-form')
    const output = document.getElementById('output')
    const loading = document.getElementById('loading')


    form.addEventListener('submit', async (e) => {
        e.preventDefault()
        loading.classList.remove('hidden')
        output.textContent = ''


        const data = {
            prompt: document.getElementById('prompt').value,
            content_type: document.getElementById('content_type').value,
            length: document.getElementById('length').value,
            temperature: document.getElementById('temperature').value,
        }


        try {
            const resp = await fetch('/api/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            })


            const json = await resp.json()
            loading.classList.add('hidden')


            if (!resp.ok) {
                output.textContent = '⚠️ Error: ' + (json.error || resp.status)
                output.classList.add('text-red-600')
                return
            }


            output.textContent = json.result
            output.classList.remove('text-red-600')
        } catch (err) {
            loading.classList.add('hidden')
            output.textContent = '⚠️ Network or unexpected error: ' + err.message
            output.classList.add('text-red-600')
        }
    })
})