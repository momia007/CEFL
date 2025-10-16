-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-09-2025 a las 23:57:59
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cflmb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `id_alumno` int(11) NOT NULL,
  `dni` varchar(20) DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT 1,
  `fecha_egreso` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos_cursos`
--

CREATE TABLE `alumnos_cursos` (
  `id_alumno` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  `fecha_inscripcion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargos`
--

CREATE TABLE `cargos` (
  `id_cargo` int(11) NOT NULL,
  `nombre_cargo` varchar(50) DEFAULT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

CREATE TABLE `cursos` (
  `id_curso` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `nikname` varchar(100) NOT NULL COMMENT 'nombre para mostrar',
  `descripcion` text DEFAULT NULL,
  `cuatrimestre` tinyint(4) NOT NULL,
  `anio` year(4) NOT NULL,
  `modalidad` enum('anual','cuatrimestral') NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1,
  `hora_inicio` time NOT NULL,
  `hora_fin` time NOT NULL,
  `dias` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cursos`
--

INSERT INTO `cursos` (`id_curso`, `nombre`, `nikname`, `descripcion`, `cuatrimestre`, `anio`, `modalidad`, `activo`, `hora_inicio`, `hora_fin`, `dias`) VALUES
(1, 'ASISTENTE DE OFICINA', 'ASISTENTE DE OFICINA', 'Curso \"A\"', 2, '2025', 'cuatrimestral', 1, '00:00:00', '00:00:00', NULL),
(2, 'ASISTENTE DE OFICINA', 'ASISTENTE DE OFICINA', 'Curso \"B\"', 2, '2025', 'cuatrimestral', 1, '00:00:00', '00:00:00', NULL),
(3, 'ASISTENTE DE OFICINA', 'ASISTENTE DE OFICINA', 'Curso \"C\"', 2, '2025', 'cuatrimestral', 1, '00:00:00', '00:00:00', NULL),
(4, 'ASISTENTE DE OFICINA', 'ASISTENTE DE OFICINA', 'Curso \"D\"', 2, '2025', 'cuatrimestral', 1, '00:00:00', '00:00:00', NULL),
(5, 'ASISTENTE DE OFICINA CON ORIENTACION EN SECRETARIADO ADMINISTRATIVO', 'ASIST. OF. EN SECRETARIADO ADMINISTRATIVO', 'Curso \"A\"', 2, '2025', 'cuatrimestral', 1, '00:00:00', '00:00:00', NULL),
(6, 'ASISTENTE DE OFICINA CON ORIENTACION EN SECRETARIADO ADMINISTRATIVO', 'ASIST. OF. EN SECRETARIADO ADMINISTRATIVO', 'Curso \"B\"', 2, '2025', 'cuatrimestral', 1, '00:00:00', '00:00:00', NULL),
(7, 'AUXILIAR PANADERO', 'PANADERO', NULL, 2, '2025', 'anual', 1, '16:00:00', '20:00:00', NULL),
(8, 'AUXILIAR EN INSTALACIONES SANITARIAS Y DE GAS DOMICILIARIA - NIVEL I', 'AUXILIAR EN INSTALACIONES SANITARIAS', NULL, 2, '2025', 'cuatrimestral', 1, '08:00:00', '10:00:00', NULL),
(9, 'AUXILIAR DE FAMILIA ESPECIALIZADOS EN CUIDADOS ORIENTADO A LA ATENCION DE PERSONAS', 'AUXILIAR DE FAMILIA', NULL, 2, '2025', 'cuatrimestral', 1, '10:00:00', '12:00:00', NULL),
(10, 'MONTADOR ELECTRICISTA DOMICILIARIO - NIVEL II', 'MONTADOR ELECTRICISTA DOMICILIARIO', NULL, 2, '2025', 'cuatrimestral', 1, '10:00:00', '12:00:00', 'Lunes,Martes,Miercoles,Jueves');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos_docentes`
--

CREATE TABLE `cursos_docentes` (
  `id_personal` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `curso_dias`
--

CREATE TABLE `curso_dias` (
  `id` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  `dia` enum('Lunes','Martes','Miércoles','Jueves','Viernes','Sábado') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paises`
--

CREATE TABLE `paises` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paises`
--

INSERT INTO `paises` (`id`, `nombre`) VALUES
(1, 'Argentina'),
(5, 'Bolivia'),
(3, 'Brasil'),
(2, 'Chile'),
(9, 'Otro'),
(6, 'Paraguay'),
(8, 'Perú'),
(4, 'Uruguay'),
(7, 'Venezuela');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal`
--

CREATE TABLE `personal` (
  `id_personal` int(11) NOT NULL,
  `dni` varchar(20) DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personal_cargos`
--

CREATE TABLE `personal_cargos` (
  `id_personal` int(11) NOT NULL,
  `id_cargo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `provincias`
--

CREATE TABLE `provincias` (
  `id` int(11) NOT NULL,
  `nombre` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `provincias`
--

INSERT INTO `provincias` (`id`, `nombre`) VALUES
(1, 'Buenos Aires'),
(2, 'Catamarca'),
(3, 'Chaco'),
(4, 'Chubut'),
(5, 'Ciudad Autónoma de Buenos Aires'),
(6, 'Córdoba'),
(7, 'Corrientes'),
(8, 'Entre Ríos'),
(9, 'Formosa'),
(10, 'Jujuy'),
(11, 'La Pampa'),
(12, 'La Rioja'),
(13, 'Mendoza'),
(14, 'Misiones'),
(15, 'Neuquén'),
(16, 'Río Negro'),
(17, 'Salta'),
(18, 'San Juan'),
(19, 'San Luis'),
(20, 'Santa Cruz'),
(21, 'Santa Fe'),
(22, 'Santiago del Estero'),
(23, 'Tierra del Fuego'),
(24, 'Tucumán');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `nombre_rol` varchar(50) DEFAULT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT current_timestamp(),
  `activo` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_roles`
--

CREATE TABLE `usuario_roles` (
  `id_usuario` int(11) NOT NULL,
  `id_rol` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`id_alumno`),
  ADD UNIQUE KEY `dni` (`dni`);

--
-- Indices de la tabla `alumnos_cursos`
--
ALTER TABLE `alumnos_cursos`
  ADD PRIMARY KEY (`id_alumno`,`id_curso`),
  ADD KEY `id_curso` (`id_curso`);

--
-- Indices de la tabla `cargos`
--
ALTER TABLE `cargos`
  ADD PRIMARY KEY (`id_cargo`);

--
-- Indices de la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id_curso`);

--
-- Indices de la tabla `cursos_docentes`
--
ALTER TABLE `cursos_docentes`
  ADD PRIMARY KEY (`id_personal`,`id_curso`),
  ADD KEY `id_curso` (`id_curso`);

--
-- Indices de la tabla `curso_dias`
--
ALTER TABLE `curso_dias`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_curso` (`id_curso`);

--
-- Indices de la tabla `paises`
--
ALTER TABLE `paises`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `personal`
--
ALTER TABLE `personal`
  ADD PRIMARY KEY (`id_personal`),
  ADD UNIQUE KEY `dni` (`dni`);

--
-- Indices de la tabla `personal_cargos`
--
ALTER TABLE `personal_cargos`
  ADD PRIMARY KEY (`id_personal`,`id_cargo`),
  ADD KEY `id_cargo` (`id_cargo`);

--
-- Indices de la tabla `provincias`
--
ALTER TABLE `provincias`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`),
  ADD UNIQUE KEY `nombre_rol` (`nombre_rol`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `usuario_roles`
--
ALTER TABLE `usuario_roles`
  ADD PRIMARY KEY (`id_usuario`,`id_rol`),
  ADD KEY `id_rol` (`id_rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `id_alumno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cargos`
--
ALTER TABLE `cargos`
  MODIFY `id_cargo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id_curso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `curso_dias`
--
ALTER TABLE `curso_dias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `paises`
--
ALTER TABLE `paises`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `personal`
--
ALTER TABLE `personal`
  MODIFY `id_personal` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alumnos_cursos`
--
ALTER TABLE `alumnos_cursos`
  ADD CONSTRAINT `alumnos_cursos_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumnos` (`id_alumno`),
  ADD CONSTRAINT `alumnos_cursos_ibfk_2` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`);

--
-- Filtros para la tabla `cursos_docentes`
--
ALTER TABLE `cursos_docentes`
  ADD CONSTRAINT `cursos_docentes_ibfk_1` FOREIGN KEY (`id_personal`) REFERENCES `personal` (`id_personal`),
  ADD CONSTRAINT `cursos_docentes_ibfk_2` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`);

--
-- Filtros para la tabla `curso_dias`
--
ALTER TABLE `curso_dias`
  ADD CONSTRAINT `curso_dias_ibfk_1` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`);

--
-- Filtros para la tabla `personal_cargos`
--
ALTER TABLE `personal_cargos`
  ADD CONSTRAINT `personal_cargos_ibfk_1` FOREIGN KEY (`id_personal`) REFERENCES `personal` (`id_personal`),
  ADD CONSTRAINT `personal_cargos_ibfk_2` FOREIGN KEY (`id_cargo`) REFERENCES `cargos` (`id_cargo`);

--
-- Filtros para la tabla `usuario_roles`
--
ALTER TABLE `usuario_roles`
  ADD CONSTRAINT `usuario_roles_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  ADD CONSTRAINT `usuario_roles_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
