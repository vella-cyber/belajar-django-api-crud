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
  // State untuk menyimpan data mahasiswa dari Django
  const [mahasiswa, setMahasiswa] = useState([]);

  // Fungsi untuk mengambil data dari API Django
  const ambilData = () => {
    fetch('http://127.0.0.1:8000/api/mahasiswa/')
      .then((response) => response.json())
      .then((hasil) => {
        setMahasiswa(hasil.data);
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
      <Box textalign="center" sx={{ mb: 4, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Typography variant="h3" component="h1" gutterBottom sx={{ fontWeight: 'bold', color: '#333' }}>
          Data Mahasiswa
        </Typography>
        <Typography variant="subtitle1" color="textSecondary">
          Integrasi React.js dengan Django API
        </Typography>
      </Box>

      {/* Tabel Data Mahasiswa */}
      <TableContainer component={Paper} elevation={3} sx={{ borderRadius: 2 }}>
        <Table sx={{ minWidth: 650 }} aria-label="tabel mahasiswa">
          <TableHead sx={{ backgroundColor: '#fafafa' }}>
            <TableRow>
              <TableCell sx={{ fontWeight: 'bold', color: '#666' }}>ID</TableCell>
              <TableCell sx={{ fontWeight: 'bold', color: '#666' }}>Nama</TableCell>
              <TableCell sx={{ fontWeight: 'bold', color: '#666' }}>Jurusan</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {mahasiswa.map((mhs) => (
              <TableRow key={mhs.id} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                {/* Kolom ID */}
                <TableCell>{mhs.id}</TableCell>
                
                {/* Kolom Nama dengan Avatar Bulat */}
                <TableCell>
                  <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                    <Avatar sx={{ bgcolor: '#bdbdbd' }}>
                      {mhs.nama ? mhs.nama.charAt(0).toUpperCase() : 'M'}
                    </Avatar>
                    <Typography sx={{ color: '#555' }}>{mhs.nama}</Typography>
                  </Box>
                </TableCell>
                
                {/* Kolom Jurusan berbentuk Chip Oval Biru */}
                <TableCell>
                  <Chip 
                    label={mhs.jurusan} 
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