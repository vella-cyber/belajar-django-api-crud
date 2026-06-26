import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Typography, 
  Paper, 
  Table, 
  TableBody, 
  TableCell, 
  TableContainer, 
  TableHead, 
  TableRow, 
  Avatar, 
  Chip, 
  Box 
} from '@mui/material';

function App() {
  // State untuk menyimpan data asisten dari Django
  const [asisten, setAsisten] = useState([]);

  // Fungsi untuk mengambil data dari API Django
  const ambilData = () => {
  fetch('http://127.0.0.1:8000/api/asisten/') // Ganti 'mahasiswa' menjadi 'asisten'
    .then((response) => response.json())
    .then((hasil) => {
      setAsisten(hasil.data);
    })
    .catch((error) => console.error("Gagal mengambil data:", error));
};

  // Jalankan fungsi ambilData saat halaman pertama kali dibuka
  useEffect(() => {
    ambilData();
  }, []);

  return (
    <Container maxWidth="md" sx={{ mt: 5, mb: 5 }}>
      {/* Bagian Judul Atas */}
      <Box textAlign="center" sx={{ mb: 4, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Typography variant="h3" component="h1" gutterBottom sx={{ fontWeight: 'bold', color: '#333' }}>
          Data Asisten Praktikum
        </Typography>
        <Typography variant="subtitle1" color="textSecondary">
          Integrasi React.js dengan Django API
        </Typography>
      </Box>

      {/* Tabel Data Asisten Praktikum */}
      <TableContainer component={Paper} elevation={3} sx={{ borderRadius: 2 }}>
        <Table sx={{ minWidth: 650 }} aria-label="tabel asisten">
          <TableHead sx={{ backgroundColor: '#fafafa' }}>
            <TableRow>
              <TableCell sx={{ fontWeight: 'bold', color: '#666' }}>ID</TableCell>
              <TableCell sx={{ fontWeight: 'bold', color: '#666' }}>Nama Asisten</TableCell>
              <TableCell sx={{ fontWeight: 'bold', color: '#666' }}>Asisten Praktikum</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {asisten.map((ast) => (
              <TableRow key={ast.id} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                {/* Kolom ID */}
                <TableCell>{ast.id}</TableCell>
                
                {/* Kolom Nama Asisten dengan Avatar Bulat */}
                <TableCell>
                  <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                    <Avatar sx={{ bgcolor: '#bdbdbd' }}>
                      {ast["nama asisten"] ? ast["nama asisten"].charAt(0).toUpperCase() : 'A'}
                    </Avatar>
                    <Typography sx={{ color: '#555' }}>{ast["nama asisten"]}</Typography>
                  </Box>
                </TableCell>
                
                {/* Kolom Asisten Praktikum berbentuk Chip Oval Biru */}
                <TableCell>
                  <Chip 
                    label={ast["asisten praktikum"]} 
                    variant="outlined" 
                    color="primary" 
                    sx={{ borderRadius: '16px', fontWeight: 500 }}
                  />
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
}

export default App;