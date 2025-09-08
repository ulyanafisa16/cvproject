if (!window.skillsLoaded) {
    window.skillsLoaded = true;

    fetch('http://127.0.0.1:8000/api/profiles/')
        .then(res => res.json())
        .then(data => {
            if (data.length > 0) {
                const profile = data[0];

                
                if (profile.image) {
                    let imgUrl = profile.image;
                    if (!imgUrl.startsWith('http')) {
                        if (!imgUrl.startsWith('/')) {
                            imgUrl = '/' + imgUrl;
                        }
                        imgUrl = `http://127.0.0.1:8000${imgUrl}`;
                    }
                    document.getElementById('profile-image').src = imgUrl;
                }

              
                document.getElementById('name').textContent = profile.name;
                document.getElementById('address').textContent = profile.address;
                document.getElementById('email').textContent = profile.email;
                document.getElementById('phone').textContent = profile.phone;
                document.getElementById('github').textContent = profile.github;
                document.getElementById('summary').textContent = profile.summary;

                
                const skillsContainer = document.getElementById('skills');
                if (skillsContainer) {
                    skillsContainer.innerHTML = '';
                    profile.skills.forEach(skill => {
                        let li = document.createElement('li');
                        li.textContent = skill.name;
                        skillsContainer.appendChild(li);
                    });
                }

              
                const educationsContainer = document.getElementById('edu');
                if (educationsContainer && profile.educations) {
                    educationsContainer.innerHTML = '';
                    profile.educations.forEach(edu => {
                        let li = document.createElement('li');
                        li.textContent = `${edu.start_year} - ${edu.end_year} | ${edu.degree} - ${edu.institution} (GPA: ${edu.gpa})`;
                        educationsContainer.appendChild(li);
                    });
                }
                    
               const organizationContainer = document.getElementById('organization-list');
                if (organizationContainer) {
                    organizationContainer.innerHTML = '';
                    if (profile.organizations && profile.organizations.length > 0) {
                        profile.organizations.forEach(org => {
                            let orgDiv = document.createElement('div');
                            orgDiv.className = 'swiper-slide';
                            orgDiv.innerHTML = `
                                <div class="card testimonials-inner">
                                    <div class="card-body">
                                        <p class="card-text mb-2">${org.description || ''}</p>
                                        <div class="testimonial-author">
                                            <div class="author-detail">
                                                <h3 class="name m-0">${org.role || ''}</h3>
                                                <span class="author-title text-primary">${org.organization || ''} (${org.period || ''})</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            `;
                            organizationContainer.appendChild(orgDiv);
                        });
                    } else {
                        organizationContainer.innerHTML = '<p class="text-center">Tidak ada data organisasi.</p>';
                    }
                }


                
                const projectsList = document.getElementById('projects-list');
                projectsList.innerHTML = '';

                profile.projects.forEach(proj => {
                    let slide = document.createElement('div');
                    slide.className = 'swiper-slide';

                    let figure = document.createElement('figure');
                    figure.className = 'portfolio-item';

                    let imageUrl = proj.image1 || proj.image2 || proj.image3 || '';
                    if (imageUrl) {
                        if (!imageUrl.startsWith('http')) {
                            if (!imageUrl.startsWith('/')) {
                                imageUrl = '/' + imageUrl;
                            }
                            imageUrl = `http://127.0.0.1:8000${imageUrl}`;
                        }

                        let link = document.createElement('a');
                        link.href = `/project/${proj.id}/`;

                        let img = document.createElement('img');
                        img.src = imageUrl;
                        img.className = 'portfolio-image';
                        img.alt = proj.title;

                        link.appendChild(img);
                        figure.appendChild(link);
                    }

                    let figcaption = document.createElement('figcaption');
                    figcaption.className = 'portfolio-title my-3 text-center';

                    let titleLink = document.createElement('a');
                    titleLink.href = `/project/${proj.id}/`;
                    titleLink.style.textDecoration = 'none';
                    titleLink.style.color = 'inherit';
                    titleLink.textContent = proj.title;

                    figcaption.appendChild(titleLink);
                    figure.appendChild(figcaption);

                    slide.appendChild(figure);
                    projectsList.appendChild(slide);
                });

                
                new Swiper('.portfolio-carousel', {
                    navigation: {
                        nextEl: '.portfolio-carousel-next',
                        prevEl: '.portfolio-carousel-prev',
                    },
                    slidesPerView: 3,
                    spaceBetween: 30,
                    loop: true,
                    breakpoints: {
                        320: { slidesPerView: 1 },
                        576: { slidesPerView: 2 },
                        992: { slidesPerView: 3 },
                    },
                });
            }
        })
        .catch(err => {
            console.error('Error loading profile data:', err);
        });

      
}