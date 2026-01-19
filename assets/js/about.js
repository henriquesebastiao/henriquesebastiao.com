// Icons provided by https://devicon.dev/
const tools = [
    // Languages, frameworks and tools
    { icon: 'python', isClickable: false },
    { icon: 'fastapi', isClickable: false },
    { icon: 'django', isClickable: false },
    { icon: 'streamlit', isClickable: false },
    { icon: 'cplusplus', tag: 'c', hint: 'C++', isClickable: false },
    { icon: 'c', tag: 'c', hint: 'C', isClickable: false },
    { icon: 'javascript', hint: 'JavaScript', isClickable: false },
    { icon: 'typescript', hint: 'TypeScript', isClickable: false },
    { icon: 'html5', tag: 'html', hint: 'HTML', isClickable: false },
    { icon: 'css3', tag: 'css', hint: 'CSS', isClickable: false },
    { icon: 'bootstrap', isClickable: false },
    { icon: 'tailwindcss', isClickable: false },
    { icon: 'arduino', isClickable: false },
    { icon: 'poetry', isClickable: false },
    { icon: 'pypi', isClickable: false },
    { icon: 'pytest', hint: 'PyTest', isClickable: false },
    { icon: 'sqlalchemy', isClickable: false },

    // Host, deployment and CI/CD
    { icon: 'docker' },
    { icon: 'podman', isClickable: false },
    { icon: 'kubernetes', isClickable: false },
    { icon: 'amazonwebservices', hint: 'AWS', isClickable: false },
    { icon: 'azure', isClickable: false },
    { icon: 'apache', isClickable: false },
    { icon: 'nginx', isClickable: false },
    { icon: 'github', hint: 'GitHub', isClickable: false },
    { icon: 'gitlab', hint: 'GitLab', isClickable: false },
    { icon: 'cloudflare', isClickable: false },

    // IDEs, editors, and tools
    { icon: 'vscode', hint: 'Visual Studio Code', isClickable: false },
    { icon: 'git', isClickable: false },
    { icon: 'jekyll', isClickable: false },
    { icon: 'markdown', isClickable: false },

    // Databases
    { icon: 'sqlite', hint: 'SQLite', isClickable: false },
    { icon: 'mysql', hint: 'MySQL', isClickable: false },
    { icon: 'postgresql', hint: 'PostgreSQL', isClickable: false },
    { icon: 'mongodb', hint: 'MOngoDB', isClickable: false },

    // Testing tools
    { icon: 'playwright', isClickable: false },
    { icon: 'selenium', isClickable: false },
    { icon: 'postman', isClickable: false },

    // Others
    { icon: 'powershell', isClickable: false },
    { icon: 'linux' },
    { icon: 'archlinux', isClickable: false },
    { icon: 'bash', isClickable: false },
    { icon: 'raspberrypi', hint: 'Raspberry Pi', isClickable: false },
    { icon: 'opentelemetry', hint: 'OpenTelemetry', isClickable: false },
    { icon: 'tex', tag: 'latex', isClickable: false },
];

const container = document.getElementById('tools');

tools.forEach((tool) => {
    const icon = tool.icon;
    const iconType = tool.iconType ?? 'plain';
    const tag = tool.tag ?? icon;
    const title = tool.hint ?? tool.icon;
    const isClickable = tool.isClickable ?? true;

    const anchor = document.createElement('a');
    const classes = isClickable ? ['tool'] : ['tool', 'disabled'];
    anchor.classList.add(...classes);
    if (isClickable) {
        anchor.href = `/tags/${tag}`;
    }
    anchor.title = title.charAt(0).toUpperCase() + title.slice(1);

    const content = document.createElement('i');
    content.className = `tool-icon devicon-${icon}-${iconType}`;

    anchor.appendChild(content);
    container.appendChild(anchor);
});

document.querySelectorAll('.tool-icon').forEach((ti) => {
    ['mouseenter', 'touchstart'].forEach((event) =>
        ti.addEventListener(
            event,
            () => {
                ti.classList.add('colored');
                ti.parentElement.classList.add('hovered');
            },
            { passive: true }
        )
    );
    ['mouseleave', 'touchend', 'touchcancel'].forEach((event) =>
        ti.addEventListener(
            event,
            () => {
                ti.classList.remove('colored');
                ti.parentElement.classList.remove('hovered');
            },
            { passive: true }
        )
    );
});