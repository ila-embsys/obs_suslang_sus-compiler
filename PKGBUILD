pkgname=sus-compiler
pkgver=0
pkgrel=0
pkgdesc="A new Hardware Design Language that keeps you in the driver's seat"
arch=('x86_64')
url="https://github.com/pc2/sus-compiler"
license=('GPL3')
groups=('base-devel')
makedepends=(
    'cargo'
    'rust'
)
source=(
    ${pkgname}-${pkgver}.tar.gz
    vendor.tar.zst
    0002-do-not-install-sus-libs-to-bin-directory.patch
)
noextract=(vendor.tar.zst)

  # About indentation: https://github.com/openSUSE/obs-service-set_version/issues/47
  sha256sums=(
    "SKIP"
    "SKIP"
    "SKIP"
  )

prepare() {
    tar -xf "${srcdir}"/vendor.tar.zst --directory "${srcdir}"/${pkgname}-${pkgver}

    cd "${srcdir}"/${pkgname}-${pkgver}

    patch --forward --strip=1 --input="${srcdir}/0002-do-not-install-sus-libs-to-bin-directory.patch"
}

build() {
  cd "${srcdir}"/${pkgname}-${pkgver}

  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target

  export SUS_COMPILER_STD_LIB_PATH=/usr/share/sus_compiler/stl

  cargo build --offline --release
}

check() {
  cd "${srcdir}"/${pkgname}-${pkgver}

  export RUSTUP_TOOLCHAIN=stable

  export SUS_COMPILER_STD_LIB_PATH=/usr/share/sus_compiler/stl

  cargo test --offline
}

package() {
  cd "${srcdir}"/${pkgname}-${pkgver}

  export RUSTUP_TOOLCHAIN=stable
  
  export SUS_COMPILER_STD_LIB_PATH=/usr/share/sus_compiler/stl

  cargo install --no-track --offline --root "$pkgdir/usr/" --path .

  install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/sus_compiler"

  install -D -t "$pkgdir/usr/share/sus_compiler/stl/" stl/*
}
