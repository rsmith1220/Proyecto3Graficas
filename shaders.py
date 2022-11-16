vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;
out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals * sin(time * 0)/10, 1.0)).xyz;
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * sin(time * 0)/10, 1.0);

}
'''

fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;
uniform vec3 pointLight;
uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    fragColor = texture(tex, UVs) * intensity;
}
'''

toon_shader ='''

#version 450 core

uniform vec3 lightDir;
varying vec3 normal;

void main()
{
	float intensity;
	vec4 color;
	intensity = dot(lightDir,normal);

	if (intensity > 0.95)
		color = vec4(1.0,0.5,0.5,1.0);
	else if (intensity > 0.5)
		color = vec4(0.6,0.3,0.3,1.0);
	else if (intensity > 0.25)
		color = vec4(0.4,0.2,0.2,1.0);
	else
		color = vec4(0.2,0.1,0.1,1.0);
	gl_FragColor = color;

}
'''