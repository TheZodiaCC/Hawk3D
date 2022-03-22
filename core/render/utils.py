import OpenGL.GL as GL
import OpenGL.GL.shaders as gl_shaders
import os


def load_shader(shader_file_path):
    shader_data = None

    if os.path.exists(shader_file_path):
        with open(shader_file_path, "r") as shader_data_file:
            shader_data = shader_data_file.readlines()

    return shader_data


def compile_shader(shader_vertex_data, shader_fragment_data):
    shader = gl_shaders.compileProgram(gl_shaders.compileShader(shader_vertex_data, GL.GL_VERTEX_SHADER),
                                       gl_shaders.compileShader(shader_fragment_data, GL.GL_FRAGMENT_SHADER))

    return shader
