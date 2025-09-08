// Ambil ID project dari URL
const pathParts = window.location.pathname.split('/').filter(Boolean);
const projectId = pathParts[pathParts.length - 1];

fetch('http://127.0.0.1:8000/api/profiles/')
    .then(res => res.json())
    .then(data => {
        if (data.length === 0) throw new Error("No profiles found");

        const profile = data[0]; 
        const project = profile.projects.find(p => p.id == projectId);

        if (!project) throw new Error("Project not found");

        document.getElementById('project-title').textContent = project.title;
        document.getElementById('project-description').innerHTML = project.description;
        document.getElementById('project-techstack').textContent = project.tech_stack || 'Tidak tersedia';
        document.getElementById('project-semester').textContent = project.semester ? `Semester ${project.semester}` : 'Tidak tersedia';

        const imagesContainer = document.getElementById('project-images');
        [project.image1, project.image2, project.image3].forEach(img => {
            if (img) {
                const imgElement = document.createElement('img');
                imgElement.src = img.startsWith('http') ? img : `http://127.0.0.1:8000${img}`;
                imgElement.alt = project.title;
                imgElement.style.maxWidth = "350px";
                imgElement.style.margin = "10px auto";
                imgElement.style.display = "block";
                imgElement.style.border = "5px solid #ccc";
                imgElement.style.borderRadius = "10px";
                imagesContainer.appendChild(imgElement);
            }
        });
    })
    .catch(err => {
        console.error("Error loading project:", err);
        document.getElementById('project-title').textContent = "Error loading project";
    });